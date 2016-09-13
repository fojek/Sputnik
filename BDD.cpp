#include <fstream>
#include <iomanip>
#include <iostream>
#include <mysql/mysql.h>

using namespace std

MYSQL *connection, mysql;
MYSQL_RES *res;
MYSQL_ROW row;
int query_state, a;

int main(){
	mysql_init(&mysql);
	connection = mysql_real_connect(&mysql, "localhost", "root", "cabane", "cabaneDB", 0, 0, 0);
	if(connection == NULL) cout << mysql_error(&mysql) << endl;

	query_state = mysql_query(connection, "select * from temperature");

	if(query_state != 0){
	  cout << mysql_error(connection) << endl << endl;
	  return 1;
	}

	res = mysql_store_result(connection);
	cout << "Les donnees de temperature entrees :" << endl << endl;

	while((row = mysql_fetch_row(res)) != NULL){
	  cout << left;
	  cout << setw(18) << row[0] << endl;
	}

	cout << endl << endl;
	return 0;
}
