import logging

from dotenv import load_dotenv

if __name__ == '__main__':
	load_dotenv()
	logging.basicConfig(
		level = logging.INFO,
		format = '[{levelname}]: {message}',
		style = '{'
	)

	logging.info(msg = '処理が正常に終了しました。')