#
# GET /api/guestbook/<guestbook_name>/greeting
#     return JSON: guestbookname as STRING, more as BOOL, next_cursor as STRING,
# 20 lastest greetings
#     GET /api/guestbook/<guestbook_name>/greeting?cursor=<urlsafe_next_cursor>
#         return 20 next greetings
#     return Http 404 if query error
# POST /api/guestbook/<guestbook_name>/greeting
#     Create new greeting
#     Successful return Http 204
#     Fail return Http 404
#     Form invalid return Http 400
# GET /api/guestbook/<guestbook_name>/greeting/<id>
#     return JSON: greeting id, content, date, updated_by, updated_date, guestbook_name
#     return Http 404 if cannot retrieve
# PUT /api/guestbook/<guestbook_name>/greeting/<id>
#     update date greeting via parameters same as POST
#     Successful return Http 204
#     Fail return Http 404
#     Form invalid return Http 400
# DELETE /api/guestbook/<guestbook_name>/greeting/<id>
#     delete greeting
#     Successful return Http 204
#     Fail return Http 404
