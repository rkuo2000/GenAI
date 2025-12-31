import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app_api = FastAPI()

app_api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory=".")

@app_api.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 憑證生成 ---
def ensure_ssl_certs():
    cert_file = "cert.pem"
    key_file = "key.pem"
    
    if not os.path.exists(cert_file) or not os.path.exists(key_file):
        print("正在生成臨時 SSL 憑證以供手機連線...")
        from OpenSSL import crypto
        
        # 生成金鑰 (RSA 2048位元)
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)
        
        # 生成憑證
        cert = crypto.X509()
        # 設定主體資訊
        cert.get_subject().C = "TW"
        cert.get_subject().ST = "Taipei"
        cert.get_subject().L = "Taipei"
        cert.get_subject().O = "rPPG Lab"
        cert.get_subject().CN = "127.0.0.1"
        
        cert.set_serial_number(1000)
        
        # 修正處：改用 set_notBefore 和 set_notAfter
        # 時間格式為 YYYYMMDDhhmmssZ (Z 代表 UTC)
        cert.set_notBefore(b"20230101000000Z") 
        cert.set_notAfter(b"20300101000000Z")
        
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')
        
        # 寫入檔案
        with open(cert_file, "wb") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        with open(key_file, "wb") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
        print("憑證生成完畢。")
        
    return cert_file, key_file

if __name__ == "__main__":
    c_file, k_file = ensure_ssl_certs()
    # 確保手機連線使用 HTTPS
    uvicorn.run(
        app_api, 
        host="0.0.0.0", 
        port=8000, 
        ssl_certfile=c_file, 
        ssl_keyfile=k_file
    )
