from nose.tools import *
from bank_transactions.parser import ParseRabobank, ParseKnab
from bank_transactions import parser

# rabobank_file = 'tests/transactions_rabobank.csv'
knab_file = 'tests/transactions_knab.csv'
bank = 'knab'


def test_parse_knab():
    parse_knab = ParseKnab()
    trans = parse_knab.transactions(knab_file)
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
    
def test_main():
    trans = parser.main(bank, knab_file)
    assert_equal(len(trans.trans), 64)