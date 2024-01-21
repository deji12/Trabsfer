from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Globals.models import Rate, Transaction
from Receipient.models import UserRecipient
from django.conf import settings
from django.core.mail import EmailMessage
import uuid

@login_required
def Home(request):

    naira = Rate.objects.get(currency_name='Nigerian naira')
    rouble = Rate.objects.get(currency_name='Russian rouble')

    if request.method == 'POST':
        
        amount = request.POST.get('amount')
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        new_transaction = Transaction(
            user = request.user,
            from_currency = from_currency,
            to_currency = to_currency,
            amount = amount,
            transaction_id=uuid.uuid4()
        )
        new_transaction.save()
        return redirect('select-recipient', transaction_id=new_transaction.transaction_id)

    context = {
        "naira": naira.rate,
        "rouble": rouble.rate,
    }

    return render(request,"send-money.html", context)

@login_required
def SelectRecipient(request, transaction_id):

    get_transaction = Transaction.objects.get(transaction_id=transaction_id, user=request.user)
    rate = Rate.objects.get(currency_name=get_transaction.from_currency)

    if request.method == "POST":

        selected_recipient = request.POST.get('selected_recipient')
        account_name = request.POST.get('account_name')
        bank_name = request.POST.get('bank_name')

        # selects a receipient
        if selected_recipient:
            get_receipient_by_account_name = UserRecipient.objects.get(user=request.user, transfer_type=get_transaction.to_currency, account_name=selected_recipient)
            get_transaction.receipient = get_receipient_by_account_name
            get_transaction.has_receipient = True

            get_transaction.current_exchange_rate = rate.rate
            get_transaction.converted_amount = get_transaction.amount * rate.rate

            get_transaction.save()

            return redirect('confirm-transaction', transaction_id=transaction_id)            
        
        # creates a new receipient and selects them
        elif account_name:
            # russian account
            if get_transaction.to_currency == "Russian rouble":
                card_number = request.POST.get('card_number')
                phone_number = request.POST.get('phone_number')

                russian_account_receipient = UserRecipient(
                    user = request.user,
                    bank_name = bank_name,
                    account_name = account_name,
                    transfer_type = get_transaction.to_currency
                )
                if phone_number:
                    russian_account_receipient.phone_number = phone_number,
                else:
                    russian_account_receipient.card_number = card_number
                russian_account_receipient.save()

                get_transaction.receipient = russian_account_receipient
                get_transaction.has_receipient = True

                get_transaction.current_exchange_rate = rate.rate
                get_transaction.converted_amount = get_transaction.amount * rate.rate

                get_transaction.save()

                return redirect('confirm-transaction', transaction_id=transaction_id)

            # naira account
            else:
                account_number = request.POST.get('account_number')

                naira_account_receipient = UserRecipient(
                    user = request.user,
                    bank_name = bank_name,
                    account_number = account_number,
                    account_name = account_name,
                    transfer_type = get_transaction.to_currency
                )
                naira_account_receipient.save()
                
                get_transaction.receipient = naira_account_receipient
                get_transaction.has_receipient = True

                get_transaction.current_exchange_rate = rate.rate
                get_transaction.converted_amount = get_transaction.amount * rate.rate

                get_transaction.save()

                return redirect('confirm-transaction', transaction_id=transaction_id)
            

    recipients = UserRecipient.objects.filter(user=request.user, transfer_type=get_transaction.to_currency)

    context = {
        "recipients": recipients
    }
    if get_transaction.to_currency == "Russian rouble":
        context['add_type'] = "russia"
    elif get_transaction.to_currency == "Nigerian naira":
        context['add_type'] = "naira"
    return render(request,"recipient.html", context)

@login_required
def ConfirmTransaction(request, transaction_id):

    get_transaction = Transaction.objects.get(transaction_id=transaction_id, user=request.user)

    if request.method == "POST":
        account_name = request.POST.get('account_name')
        bank_name = request.POST.get('bank_name')


        if account_name:
            # russian account
            if get_transaction.to_currency == "Russian rouble":
                card_number = request.POST.get('card_number')
                phone_number = request.POST.get('phone_number')

                russian_account_receipient = get_transaction.receipient
                russian_account_receipient.bank_name = bank_name
                russian_account_receipient.account_name = account_name

                if phone_number:
                    russian_account_receipient.phone_number = phone_number,
                else:
                    russian_account_receipient.card_number = card_number
                russian_account_receipient.save()

                return redirect('confirm-transaction', transaction_id=transaction_id)

            # naira account
            else:
                account_number = request.POST.get('account_number')

                naira_account_receipient = get_transaction.receipient
                naira_account_receipient.bank_name = bank_name
                naira_account_receipient.account_name = account_name
                naira_account_receipient.account_number = account_number

                naira_account_receipient.save()

                return redirect('confirm-transaction', transaction_id=transaction_id)

    context = {
        "transaction": get_transaction
    }

    return render(request,"confirm.html", context)

@login_required
def ChangeTransactionAmount(request, transaction_id): 

    get_transaction = Transaction.objects.get(transaction_id=transaction_id, user=request.user)
    rate = Rate.objects.get(currency_name=get_transaction.from_currency)

    if request.method == 'POST':
        
        amount = request.POST.get('amount')
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        get_transaction.from_currency = from_currency
        get_transaction.to_currency = to_currency
        get_transaction.amount = amount

        get_transaction.current_exchange_rate = rate.rate
        get_transaction.converted_amount = float(amount) * rate.rate

        get_transaction.save()
        return redirect('confirm-transaction', transaction_id=transaction_id)

    naira = Rate.objects.get(currency_name='Nigerian naira')
    rouble = Rate.objects.get(currency_name='Russian rouble')

    context = {
        "naira": naira.rate,
        "rouble": rouble.rate,
        "transaction": get_transaction
    }

    return render(request,"edit_transaction_amount.html", context)

def ConfirmedPayment(request, transaction_id):

    get_transaction = Transaction.objects.get(transaction_id=transaction_id, user=request.user)
    get_transaction.paid = True
    get_transaction.save()

    naira_transaction_message = f"Transaction ID: {transaction_id}\n\nUser: {get_transaction.user.get_full_name()}\n\nType: {get_transaction.from_currency} --> {get_transaction.to_currency}\n\nPaid amount: {get_transaction.amount} {get_transaction.from_currency}\n\nConverted to {get_transaction.converted_amount} {get_transaction.to_currency}\n\nRate: {get_transaction.current_exchange_rate}\n\n\nReceiver Account:\nBank Name: {get_transaction.receipient.bank_name}\n\nAccount Name: {get_transaction.receipient.account_name}\n\nAccount Number: {get_transaction.receipient.account_number}  \n\n\nDate: {get_transaction.date}"
    rouble_transaction_message = f"Transaction ID: {transaction_id}\n\nUser: {get_transaction.user.get_full_name()}\n\nType: {get_transaction.from_currency} --> {get_transaction.to_currency}\n\nPaid amount: {get_transaction.amount} {get_transaction.from_currency}\n\nConverted to {get_transaction.converted_amount} {get_transaction.to_currency}\n\nRate: {get_transaction.current_exchange_rate}\n\n\nReceiver Account:\nBank Name: {get_transaction.receipient.bank_name}\n\nAccount Name: {get_transaction.receipient.account_name}\n\nCard Number: {get_transaction.receipient.card_number}\n\nPhone Number: {get_transaction.receipient.phone_number}  \n\n\nDate: {get_transaction.date}"

    email_message_content = None
    if get_transaction.to_currency == "Nigerian naira":
        email_message_content = naira_transaction_message
    else:
        email_message_content = rouble_transaction_message

    email_mess = EmailMessage (
        "New payment",
        email_message_content,
        settings.EMAIL_HOST_USER, # email sender
        [settings.PLATFORM_EMAIL_RECEIVER, get_transaction.user.email] # recipients
    )
    email_mess.fail_silently = True
    # email_mess.send()

    return redirect('transaction-successful', transaction_id=transaction_id)

@login_required
def SuccessPayment(request, transaction_id):

    get_transaction = Transaction.objects.get(transaction_id=transaction_id, user=request.user)

    context = {
        "transaction": get_transaction
    }

    return render(request, "send-money-success.html", context)

@login_required
def Transactions(request):

    get_transactions = Transaction.objects.filter(user=request.user)

    context = { 
        "transactions": get_transactions
    }

    return render(request, "transactions.html", context)

@login_required
def Recipients(request):

    get_user_recipients = UserRecipient.objects.filter(user=request.user)

    context = {
        "recipients": get_user_recipients
    }

    return render(request, "recipients.html", context)

@login_required
def DeleteTransaction(request, transaction_id):

    get_transaction = Transaction.objects.get(transaction_id=transaction_id)
    get_transaction.delete()

    return redirect('transactions')

def EditRecipientData(request, _id):

    try:
        get_recipient = UserRecipient.objects.get(user=request.user, id=_id)

        if request.method == "POST":

            account_name = request.POST.get('account_name')
            bank_name = request.POST.get('bank_name')    
            card_number = request.POST.get('card_number')
            phone_number = request.POST.get('phone_number')   
            account_number = request.POST.get('account_number')
        
            if account_name:
                get_recipient.account_name = account_name
            if bank_name:
                get_recipient.bank_name = bank_name
            if card_number:
                get_recipient.card_number = card_number
            if phone_number:
                get_recipient.phone_number = phone_number
            if account_number:
                get_recipient.account_number = account_number
            
            get_recipient.save()

            return redirect('recipients')

        context = {
            'recipient': get_recipient
        }

        return render(request, "edit-recipient.html", context)
    except UserRecipient.DoesNotExist:

        return redirect('recipients')