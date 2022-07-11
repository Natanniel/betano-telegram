from time import sleep
from pynubank import Nubank, MockHttpClient


nu = Nubank()
uuid, qr_code = nu.get_qr_code()
# Nesse momento será printado o QRCode no console
# Você precisa escanear pelo o seu app do celular
# Esse menu fica em NU > Perfil > Acesso pelo site
qr_code.print_ascii(invert=True)
#input('Enter apos a confirmacao')
# Somente após escanear o QRCode você pode chamar a linha abaixo

nu.authenticate_with_qr_code('44277200800', 'Pk192168@', uuid)

print(nu.get_account_balance())
data = nu.get_available_pix_keys()

code = '123' #Código único da tansação é necessário para o get_pix_identifier

print(data['keys']) # Retorna lista de chaves cadastradas no Pix

print(data['account_id']) # Retorna id da sua conta

# No exemplo abaixo solicitamos uma cobrança de R$ 50,25 utilizando a primeira chave cadastrada
money_request = nu.create_pix_payment_qrcode(data['account_id'], 50.25, data['keys'][0], code)

# Irá printar o QRCode no terminal
money_request['qr_code'].print_ascii()

# Também é possível gerar uma imagem para ser enviada através de algum sistema
# Nesse caso irá salvar um arquivo qr_code.png que pode ser escaneado pelo app do banco para ser pago
# Salva o nome do arquivo com o código do identifier
qr = money_request['qr_code']
img = qr.make_image()
img.save(code+'.png')

# Além do QRCode também há uma URL para pagamento
print(money_request['payment_url'])