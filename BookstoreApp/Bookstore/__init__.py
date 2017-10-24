from flask import Flask, render_template, request
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError, AutoReconnect
from DbService import DbService, Paging
import commands
import ipaddress

app = Flask(__name__)
db_service = None
web_service_addr = None


@app.route('/')
def show_books():
    global db_service, web_service_addr

    page_num = int(request.args.get('page', default=1))
    Paging.set_curr_page(page_num)

    books_for_page = db_service.get_books().find().skip((page_num - 1) * 10).limit(10)

    return render_template('index.html',
                           books=books_for_page,
                           paging=Paging.values,
                           db_addr=db_service.conn_addr,
                           web_addr=web_service_addr)


@app.route('/book/<int:book_id>')
def show_book(book_id):
    global db_service, web_service_addr

    book = db_service.get_books().find_one({'_id': book_id})

    return render_template('book.html',
                           book=book,
                           db_addr=db_service.conn_addr,
                           web_addr=web_service_addr)


# -----------------------------------------------------------------------------------------


@app.before_request
def check_if_db_available():
    global db_service
    try:
        # The ismaster command is cheap and does not require auth.
        db_service.get_mongo_client().admin.command('ismaster')
    except (ServerSelectionTimeoutError, AutoReconnect, ConnectionFailure, AttributeError):
        db_service = DbService()
        Paging.init_paging_obj(db_service)


@app.before_first_request
def find_ip():
    global web_service_addr

    def check_if_ipv4_and_private(addr):
        ip = ipaddress.ip_address(addr)
        return isinstance(ip, ipaddress.IPv4Address) and ip.is_private

    ips = map(unicode, commands.getoutput('hostname -I').strip().split())
    web_service_addr = filter(check_if_ipv4_and_private, ips)[-1]


# -----------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()
