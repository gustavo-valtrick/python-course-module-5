import sys
from pathlib import Path
_ROOT_DIR = Path(__file__).parents[1]
sys.path.append(str(_ROOT_DIR))

import pytest
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()
    
    #create a payment
    payment_info = pix_instance.create_payment(base_dir="../")
    
    assert "bank_payment_id" in payment_info
    assert "qr_code_path" in payment_info
    
    qr_code_path = payment_info["qr_code_path"] + ".png"
    assert (_ROOT_DIR / "static" / "img" / qr_code_path).is_file()