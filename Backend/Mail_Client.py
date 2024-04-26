import imaplib
import logging
import os

from dotenv import load_dotenv

if __name__ == '__main__':
	load_dotenv()
	logging.basicConfig(
		level = logging.INFO,
		format = '[{levelname}]: {message}',
		style = '{'
	)

	with imaplib.IMAP4_SSL(
		host = os.getenv(key = 'E-Mail_Domain'),
		port = 993,
		ssl_context = None,
		timeout = 30
	) as mail_client:
		mail_client.login(
			user = f"{os.getenv(key = 'E-Mail_Account')}@{os.getenv(key = 'E-Mail_Domain')}",
			password = os.getenv(key = 'E-Mail_Password')
		)

		mail_client.logout()

	logging.info(msg = '処理が正常に終了しました。')