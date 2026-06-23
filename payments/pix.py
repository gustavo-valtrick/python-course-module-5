from uuid import uuid4
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self, base_dir=""):
        #create payment at the financial institution
        bank_payment_id = str(uuid4())
        
        hash_payment = f"hash_payment_{bank_payment_id}"
        
        #qr code
        payment_qr_code = qrcode.make(hash_payment)
        
        #save image as png
        file_name = f"qr_code_payment_{bank_payment_id}"
        payment_qr_code.save(f"{base_dir}static/img/{file_name}.png")
        
        return{
            "bank_payment_id":bank_payment_id,
            "qr_code_path": file_name
            }