Title: Curl Examples for Testing API
Date: 2018-01-23 23:51
Tags: curl
Slug: curl-examples-for-testing-api

The following are just a few examples I gathered for testing a basic API I created using ASP.NET Core. I will probably edit this article later. It's getting late and I just want to retain the information for now.

<span style="color:red;">*Note: I am in a Linux environment and I'm piping a python command to prettify the returned JSON.*</span>

# GET Examples

```sh
curl localhost:5000/api/todo/ | python -m json.tool
curl localhost:5000/api/todo/1 | python -m json.tool
```

# POST Example

```sh
curl -i -X POST -H "Content-Type:application/json" localhost:5000/api/todo -d '{"Name":"New Todo Item"}'
```

# PUT Example

For PUT I found that the order of the key/value pairs in the json string have to match the order of the key/value pairs in the database.

```sh
curl -X PUT -H "Content-Type: application/json" -d '{"id":6, "isComplete":true, "name":"New Todo Item"}' localhost:5000/api/todo/6
```

# DELETE Example

```sh
curl -X "DELETE" localhost:5000/api/todo/6
```
