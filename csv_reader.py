import csv


def read_csv_file(file_path, field_names):
    """
    Đọc một tệp CSV và trả về các dòng dữ liệu dưới dạng danh sách các từ điển.
    
    Args:
    - file_path (str): Đường dẫn đến tệp CSV.
    - field_names (list): Danh sách tên các trường trong tệp CSV.
    
    Returns:
    - data (list): Danh sách các từ điển, mỗi từ điển chứa dữ liệu của một dòng trong tệp CSV.
    """
    data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file, fieldnames=field_names)
        next(reader)  # Bỏ qua dòng tiêu đề (nếu có)
        for row in reader:
            data.append(row)
    return data

titleEachHeight = ['height', 'numRound', 'numTx', 'blockSizeBytes', 'blockIntervalSeconds', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']
titleEachVote = ['height', 'roundID', 'step', 'validatorsPower', 'missingValidatorsPowerPrevote']
titleEachProposal = ['height', 'roundID', 'step', 'numblockParts', 'blockPartsReceived']
titleEachTime = ['height', 'roundID', 'stepName', 'stepTime']
titleEachP2P = ['height', 'roundID', 'step', 'fromPeer', 'toPeer', 'chID', 'msgType', 'size', 'rawByte']

def eachVote():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/blockVoteStep.csv'

    return read_csv_file(file_path, titleEachVote)

def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/block.csv'

    return read_csv_file(file_path, titleEachHeight)

def eachProposal():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/blockProposalStep.csv'

    return read_csv_file(file_path, titleEachProposal)

def eachTimeStep():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/blockOnlyTimeStep.csv'

    return read_csv_file(file_path, titleEachTime)

def eachP2P():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/blockP2P.csv'

    return read_csv_file(file_path, titleEachP2P)