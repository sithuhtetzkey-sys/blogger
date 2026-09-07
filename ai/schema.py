MOVIE_RECAP_SCHEMA = {

"type":"object",

"properties": {


"title": {

"type":"string"

},


"movie": {

"type":"object",

"properties": {

"title":{
"type":"string"
},

"year":{
"type":"integer"
},

"genre":{
"type":"array",
"items":{
"type":"string"
}

}

}

},



"hook": {

"type":"object",

"properties": {


"opening_sentence":{

"type":"string"

},


"mystery_question":{

"type":"string"

}

}

},



"characters": {

"type":"array",

"items":{

"type":"object",

"properties":{

"name":{
"type":"string"
},

"role":{
"type":"string"
},

"description":{
"type":"string"
}

}

}

},



"content_html":{

"type":"string"

},



"labels":{

"type":"array",

"items":{

"type":"string"

}

}

}


}
