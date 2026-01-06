from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def initiate(self):
        pass

    @abstractmethod
    def success(self):
        pass

    @abstractmethod
    def failure(self):
        pass

class PaypalPaymentGateway(PaymentGateway):

    def initiate(self):
        return "Initiating Paypal Payment Gateway"

    def success(self):
        return "Payment Successfull"

    def failure(self):
        return "Payment Failed"


paypal_payment_gateway = PaypalPaymentGateway()
print(paypal_payment_gateway.initiate())
print(paypal_payment_gateway.success())