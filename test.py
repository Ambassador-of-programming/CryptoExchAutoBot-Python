from time import sleep
import random
from config.token import wallets, block_chain


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
            # Генерируем случайное число
            random_number = round(random.uniform(0.000001, 0.00005), 6)
            
            # Преобразуем число в строку и удаляем лишние нули и символы
            cleaned_number = format(random_number, '.6f').rstrip('0').rstrip('.')
            print(f"Transaction Range: {transaction_range}\n"
                  f"Delay after each swap: {interval_transaction}\n"
                  f"Wallet: {wallet_random}\n"
                  f"Private Key: {private_key}\n"
                  f"Blockchain: {blockchain_random}\n"
                  f"web3RpcUrl: {web3RpcUrl}\n"
                  f"To Address: {to_address_random}\n"
                  f"Amount: {cleaned_number}\n"
                  )
            
            # sleep
            sleep(interval_transaction)
            
        else:
            # Random amount for the swap
            random_number = round(random.uniform(0.000001, 0.00005), 6)
            
            # Convert the number to a string and remove unnecessary zeros and characters
            cleaned_number = format(random_number, '.6f').rstrip('0').rstrip('.')

            print(f"Transaction Range: {transaction_range}\n"
                  f"Delay after each swap: {interval_transaction}\n"
                  f"Wallet: {wallet_random}\n"
                  f"Private Key: {private_key}\n"
                  f"Blockchain: {blockchain_random}\n"
                  f"web3RpcUrl: {web3RpcUrl}\n"
                  f"To Address: {to_address_random}\n"
                  f"Amount: {cleaned_number}\n"
                  )
            
            # sleep
            sleep(interval_transaction)

# Run the script
if __name__ == "__main__":
    swap_random(transaction_range=1, sleep_time=1)
