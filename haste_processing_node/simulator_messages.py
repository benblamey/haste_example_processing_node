import pickle


def split_data_from_simulator(message_bytes):
    # Format is a concatenation of a pickled dictionary, then the image bytes:

    metadata = pickle.loads(message_bytes)  # Note: Bytes past the pickled object’s representation are ignored.

    image_length_bytes = metadata['image_length_bytes']
    image_bytes = message_bytes[-image_length_bytes:]

    return metadata, image_bytes


if __name__ == '__main__':
    # Test
    some_bytes = b'foo'
    metadata, image_bytes = split_data_from_simulator(
        bytearray(
            pickle.dumps(
                {'foo': 123,
                 'bar': 'wibble',
                 'image_length_bytes': len(some_bytes)})
        )
        + some_bytes)

    print(metadata)
    print(image_bytes)
