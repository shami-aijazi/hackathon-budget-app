from random import randrange



# Budget account JSON definition (all numbers monthly)

# sample_account = {"id": "0",
#                   "profile": "young_professional",
#                   "balance": "100000",
#                   "income": "70000",
#                   "rent": "10000",
#                   "groceries": "10000",
#                   "transportation": "1000",
#                   "medical": "10000",
#                   "entertainment": "10000",
#                   "shopping": "10000",
#                     }



# global dict to hold all accounts by ID

def create_accounts (num_accounts):
    """
    Method to create a specified number of accounts and store them in all_accounts dict.
    :param num_accounts: number of accounts to create
    :return: dict containing the generated accounts
    """

    all_accounts = {}

    for i in range (num_accounts):
        # Generate accounts with accounts with random ranges of values
        created_account = {}

        created_account["id"] = i
        created_account["profile"] = "young professional"
        created_account["balance"] = randrange(5000, 15000)
        created_account["income"] = randrange(4000, 8000)
        created_account["rent"] = randrange(800, 1200)
        created_account["groceries"] = randrange(200, 600)
        created_account["transportation"] = randrange(150, 350)
        created_account["medical"] = randrange(100, 300)
        created_account["entertainment"] = randrange(100, 300)
        created_account["shopping"] = randrange(100, 300)
        created_account["dining"] = randrange(200, 400)
        created_account["total_expenditures"] = created_account["balance"] + created_account["income"]\
                                                + created_account["income"] + created_account["rent"] \
                                                + created_account["groceries"] + created_account["transportation"]\
                                                + created_account["medical"] + created_account["entertainment"]\
                                                + created_account["shopping"] + created_account["dining"]

        all_accounts[str(i)] = created_account # Increment ID

    return all_accounts
