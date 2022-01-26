def find_seq_and_ack_numbers(initial_ack_number: int, packets: list):
    """
    Solves problems like 'Suppose segments P, Q, and R arrive at Host B in order.
             What is the acknowledgment number on the segment sent in response to segment R?'
    :param initial_ack_number: ack number before the first packet of sizes is sent
    :param packets: list of dicts holding each packet's "name" and "size", in order sent
    :return: dict wherein keys are packet names, values are dicts in JSON format with
             sequence number, size, and ack number that should be sent in response, assuming in-order arrival
    """
    # return variable
    packet_data_out = {}

    prev_ack_number = initial_ack_number
    for packet in packets:
        # packet name
        packet_name = packet['name']

        # packet size
        packet_size = packet['size']

        # sequence number is previous packet's ack number (assuming in-order arrival and immediate ack)
        packet_seq_number = prev_ack_number

        # ack number sent in response is one more than is inside this packet
        #     (assuming in-order arrival and immediate ack)
        presumed_ack_number = packet_seq_number + packet_size

        # update prev ack for next iteration
        prev_ack_number = presumed_ack_number

        # add values to return variable
        packet_data_out[packet_name] = {
            'seq_number': packet_seq_number,
            'size': packet_size,
            'in_order_ack_number': presumed_ack_number
        }

    return packet_data_out


if __name__ == '__main__':
    # test
    initial_ack = 4402
    known_packet_data = [
        {
            'name': 'P',
            'size': 285
        },
        {
            'name': 'Q',
            'size': 409
        },
        {
            'name': 'R',
            'size': 377
        }
    ]
    full_packet_data = find_seq_and_ack_numbers(initial_ack, known_packet_data)
    print(full_packet_data)
