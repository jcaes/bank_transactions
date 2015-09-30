from nose.tools import *
from bank_transactions.parser import ParseRabobank, ParseKnab


# rabobank_file = 'tests/transactions_rabobank.csv'
knab_file = 'tests/transactions_knab.csv'
    
# def test_parse_rabobank():
#     parse_rabobank = ParseRabobank(rabobank_file)
#     parse_rabobank.run()
#     assert_equal(parse_rabobank.file, rabobank_file)
#     assert_equal(parse_rabobank.file_type, 'csv')
#     assert_equal(parse_rabobank.file_column.account, 2)
#     assert_equal(parse_rabobank.file_column.contra_account, 6)
#     assert_equal(parse_rabobank.file_column.transaction_date, 10)
#     assert_equal(parse_rabobank.file_column.amount, 3)
#     assert_equal(parse_rabobank.file_column.currency, 4)
#     assert_equal(parse_rabobank.file_column.contra_account_name, 5)
#     assert_equal(parse_rabobank.file_column.description, 8)
#     assert_equal(parse_rabobank.header_rows, 1)
#     assert_equal(parse_rabobank.date_format, "%m/%d/%Y")
#     assert_equal(parse_rabobank.debit_column, 3)
#     assert_equal(len(parse_rabobank.data), 439)
    
def test_parse_knab():
    parse_knab = ParseKnab(knab_file)
    trans = parse_knab.transactions()
    assert_equal(parse_knab.file, knab_file)
    assert_equal(parse_knab.file_type, 'csv')
    assert_equal(parse_knab.file_column.account, 0)
    assert_equal(parse_knab.file_column.contra_account, 5)
    assert_equal(parse_knab.file_column.transaction_date, 7)
    assert_equal(parse_knab.file_column.amount, 4)
    assert_equal(parse_knab.file_column.currency, 2)
    assert_equal(parse_knab.file_column.contra_account_name, 6)
    assert_equal(parse_knab.file_column.description, 9)
    assert_equal(parse_knab.header_rows, 2)
    assert_equal(parse_knab.date_format, "%d-%m-%Y")
    assert_equal(len(trans.trans), 64)