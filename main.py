from time import sleep
import random
from config.token import wallets, block_chain
from swap_a_settings import swapExampleA
from swap_p_settings import swapExampleP


def swap_random(transaction_range: int, sleep_time: int):
    # Number of transactions to perform (e.g., 10-15 transactions)
    transaction_range = transaction_range

    # Delay after each swap
    interval_transaction = sleep_time

    for _ in range(0, transaction_range):
        # Randomly select a wallet
        wallet_random = random.choice(list(wallets.keys()))
        private_key = wallets[wallet_random]

        # Randomly choose a blockchain
        blockchain_random = random.choice(list(block_chain.keys()))
        to_address_random = random.choice(block_chain[blockchain_random][1:])
        web3RpcUrl = block_chain[blockchain_random][0]['web3RpcUrl']
                
        if blockchain_random == 'Arbitrum':
            # Random amount for the swap
            random_number = round(random.uniform(0.0001, 0.005), 4)
            
            # Convert the number to a string and remove unnecessary zeros and characters
            cleaned_number = format(random_number, '.6f').rstrip('0').rstrip('.')
            swapExampleA(wallet=wallet_random, private_key=private_key,
                         web3RpcUrl=web3RpcUrl, swap_amount=cleaned_number, to_token=to_address_random)
            
            # sleep
            sleep(interval_transaction)
            
        else:
            # Random amount for the swap
            random_number = round(random.uniform(0.0001, 0.005), 4)
            
            # Convert the number to a string and remove unnecessary zeros and characters
            cleaned_number = format(random_number, '.6f').rstrip('0').rstrip('.')
            swapExampleP(wallet=wallet_random, private_key=private_key,
                         web3RpcUrl=web3RpcUrl, swap_amount=cleaned_number, to_token=to_address_random)
            
            # sleep
            sleep(interval_transaction)

# Run the script
if __name__ == "__main__":
    """
    You need to specify how many swaps to do and how long it should sleep after each swap
    """

    swap_random(transaction_range=1, sleep_time=1)
