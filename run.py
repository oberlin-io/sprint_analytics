import os
import argparse
from config import config
from sprintreview import accomplishments


def argparsing():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a',
        help="Send sprint date's accomplishments to Reports. Input sprint end date yyyy-mm-dd",
        )

    return parser.parse_args()


def get_accomplishments(conf, date):

    Acc = accomplishments.Accomplishments(
        os.getcwd(),
        conf,
        date,
        )
    Acc.get_sprint_xl()
    Acc.filter_sprint_xl()
    Acc.reduce_sprint_xl()
    Acc.sort_sprint_xl()
    Acc.format_sprint_xl()
    Acc.sprint_xl_to_txt()
    Acc.send_to_reports()
    #summary = Acc.get_txt()


def main():
    
    Conf = config.Config(os.getcwd())
    Conf.set()
    
    args = argparsing()

    if args.a is not None:
        get_accomplishments(Conf.get(), args.a)


if __name__ == '__main__':

    main()
