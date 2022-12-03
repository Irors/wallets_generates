import loguru
from web3.auto import w3
import xlsxwriter
from loguru import logger

number_wallet = int(input("How many wallets do you want to create? "))

if type(number_wallet) != int:
    loguru.logger.error("Pleas write number!")
else:
    outWorkBook = xlsxwriter.Workbook("wallets.xlsx")
    outSheet = outWorkBook.add_worksheet()

    for _ in range(number_wallet + 1):
        acct = w3.eth.account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')

        outSheet.write(f"A{_}", acct.address)
        outSheet.write(f"B{_}", acct.privateKey.hex())

    loguru.logger.success(f"Successfully created {number_wallet} wallets")
    outWorkBook.close()
