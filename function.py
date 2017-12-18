from harmonicPE import daemon


def process_message(message_bytes):
    print('process_message')


daemon.listen_for_tasks(process_message)