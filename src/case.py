import psycopg2
import psycopg2.extras


def get_all_request_cases():
    conn = psycopg2.connect(host="smax-prd-eks-postgres.co24hh8ebtxg.us-east-2.rds.amazonaws.com",
                            database="xservices_ems", user="postgresEks", password="Compecscprod9", port='5432')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    query_case_ids = 'SELECT "ID" as request_id, "NUMBEROFATTACHMENTS" as number_attachments, "REQUESTATTACHMENTS" ' \
                     'as json_attachments FROM view_716383812.request ' \
                     'where view_716383812.request."NUMBEROFATTACHMENTS" > 2 limit 3'
    cur.execute(query_case_ids)
    cases_info = cur.fetchall()
    cur.close()
    conn.close()

    return cases_info
