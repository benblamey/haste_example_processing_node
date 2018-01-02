
def split_data_from_simulator(message_bytes):
    # Issue: if pickled data contains } this will break. Use length prefix in message?
    for i in range(len(message_bytes)):
        if message_bytes[i] == "}":
            index = i+1
            break

    # TODO: use pickle deserialization here?
    return eval(message_bytes[0:index]), message_bytes[-(len(message_bytes) - index):]