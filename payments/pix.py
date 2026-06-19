from uuid import uuid4
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        #create payment at the financial institution
        bank_payment_id = str(uuid4())
        
        hash_payment = f"hash_payment_{bank_payment_id}"
        
        #qr code
        payment_qr_code = qrcode.make(hash_payment)
        
        #save image as png
        payment_qr_code_path = f"static/img/qr_code_payment_{bank_payment_id}.png"
        payment_qr_code.save(payment_qr_code_path)
        
        return{
            "bank_payment_id":bank_payment_id,
            "qr_code_path": payment_qr_code_path
            }