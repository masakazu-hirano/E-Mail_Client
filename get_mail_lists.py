import email
import imaplib

sakura_mailbox = imaplib.IMAP4_SSL(host='初期ドメイン', port=993)
sakura_mailbox.login('メールアドレス', 'パスワード')

sakura_mailbox.select(mailbox='INBOX', readonly=True)
status, response = sakura_mailbox.search('UTF-8', 'ALL')

status, mail_data = sakura_mailbox.fetch(response.split()[0], '(RFC822)')

email.message_from_string(mail_data[0][1].decode('utf-8'))['From']
  # 送信先アドレスを取得する。
email.message_from_string(mail_data[0][1].decode('utf-8'))['Subject']
  # 件名を取得する。
  # TODO: 文字化けを解消する。
