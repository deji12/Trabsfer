from django.urls import path
from . import views

urlpatterns = [
    path('send-money/', views.Home, name='dashboard'),
    path('select-recipient/<str:transaction_id>/', views.SelectRecipient, name='select-recipient'),
    path('confirm-transaction-details/<str:transaction_id>/', views.ConfirmTransaction, name='confirm-transaction'),
    path('edit-transaction-amount/<str:transaction_id>/', views.ChangeTransactionAmount, name='edit-transaction-amount'),
    path('mark-transaction-successful/<str:transaction_id>/', views.ConfirmedPayment, name='mark-transaction-successful'),
    path('transaction-successful/<str:transaction_id>/', views.SuccessPayment, name='transaction-successful'),
    path('transactions/', views.Transactions, name='transactions'),
    path('delete-transaction/<str:transaction_id>/', views.DeleteTransaction, name='delete-transaction'),
    path('recipients/', views.Recipients, name='recipients'),
    path('edit-recipient/<int:_id>/', views.EditRecipientData, name='edit-recipient'),
]