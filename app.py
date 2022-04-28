import dropbox

class TransferData:
    def __init__(self,token):
        self.token = token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    acc_tok = "sl.BFw-GxP7rPHJ12gbh76JI7u_HsHCJRvLgqXX3AaHpbv2UQcDgerS_mKwcU-_zKk4aeEOCXhJDb8nD2q8JUSDY6eIMKHYPAsMxTsd1_0aEuBIrCYJeGDLa_sVPtWxvo9qdgkrCMsrSGG2"
    file_from="sample.txt"
    file_to = "/Automate/sample.txt"

    transferData = TransferData(acc_tok)
    transferData.upload_files(file_from,file_to)
    print("Transfer successful")

main()