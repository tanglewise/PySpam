import iota
from iota import *
import time

seed = b'SSFM9SBA9GIREICDJU9FVUKZUU9KLXUWQBIIFIYHXQRMAJQHUKCKRXWFJKDJG9DCHSOIEGH9' #random seed
uri = 'http://localhost:14265' #local node
api = Iota(uri, seed)

print(api.get_node_info())

def spam(tx_num):

    api = Iota(
        'http://localhost:14265',
        seed = b'SSFM9SBA9GIREICDJU9FVUAKZUU9KLXUIFIYMAJQHUKCKRXWFJKDJG9DCHSOIEGH9'
    )
    address = api.get_new_addresses(count=5)['addresses'][3]
    address = Address(b'GOOGLE9DOT9COM999999999999999999999999999999999999')
    
    while True:
        try:
            print('start', time.time())
            proposed_tx = ProposedTransaction(
                address = address,
                value = 0,
                tag = Tag(b'999GOOGLE9DOT9COM999'),
                message = TryteString.from_unicode('google.com'))
            print('proposed', time.time())
            trytes = api.prepare_transfer(transfers=[proposed_tx])['trytes']
            print('got trytes', time.time())
            tx_to_approve = api.getTransactionsToApprove(depth=5)
            print('got txs', time.time())
            proposed_trunk = tx_to_approve['trunkTransaction']
            proposed_branch = tx_to_approve['branchTransaction']
            proposed_tx.branch_transaction_hash = proposed_branch
            proposed_tx.trunk_transaction_hash = proposed_trunk
            attachment = api.attachToTangle(trunkTransaction=proposed_trunk,
                branchTransaction=proposed_branch,
                minWeightMagnitude=14,
                trytes=trytes)

            print('attached', time.time())
            broadcast = api.broadcastTransactions(trytes=attachment['trytes'])
            print('broadcasted', time.time())
            print(proposed_tx.hash)
            print('trunk', proposed_trunk)
            print('branch', proposed_branch)
            print()
        except Exception as e:
            print(e)
        
spam(1)
