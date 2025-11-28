import pyotp
import qrcode
import base64

# Hardcoded secret string
secret = "my_very_sneaky_secret"

# Convert to Base32
secret_bytes = secret.encode("utf-8")
encoded_secret = base64.b32encode(secret_bytes).decode("utf-8")
print("Base32 Secret:", encoded_secret)

# Create a TOTP object with the Base32 secret
totp = pyotp.TOTP(encoded_secret)

# Generate provisioning URI (for Google Authenticator)
uri = totp.provisioning_uri(name="alex@example.com", issuer_name="DemoApp")

# Generate QR code
qrcode.make(uri).show()

# Verification loop
print("Current OTP:", totp.now())


