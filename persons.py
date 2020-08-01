from tools import get_session, fill_up_base, average_age, average_gender, query_popular_city, query_strong_passwords, query_popular_pass



if __name__ == '__main__':
    # fill_up_base()
    print(query_strong_passwords())
    print(query_popular_city())
    print(query_popular_pass())
    print(query_popular_city(2))
    print(query_popular_pass(2))
    print(query_popular_city(6))
    print(query_popular_pass(6))
    print(average_age())
    print(average_age('male'))
    print(average_age('female'))
    print(average_gender())
