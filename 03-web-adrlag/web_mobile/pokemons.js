const h1 = document.querySelector('h1');
const pokemon = document.querySelector('#pokemon');
const email = document.querySelector('#email');
const subject = document.querySelector('#subject');
const message = document.querySelector('#message');
const pokemonslist = document.querySelector('#pokemonslist');
const pokeInfo = document.querySelector('h2');
const show_all = document.querySelector('#show_all');
const ability = document.querySelector('#ability');
const type = document.querySelector('#type');
const stat = document.querySelector('#stats');
const datalist = document.querySelector('#allnames');
const show = document.querySelector("#show");
const send = document.querySelector('#send');
const alertdialog = document.createElement("dialog");
const MAX_POKEMONS = 50; //Pokemons totales = 898 (va muy lento al ponerlo)
const url = "https://pokeapi.co/api/v2/pokemon/";
let only_pokemon = '';
let one_pokemon = false;

const httpState = {
    // Metí solo algunos códigos que podrían llegar a darse
    // pero lo normal es que solo se de el caso del 404
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    406: "Not Acceptable",
    408: "Request Timeout",
    429: "Too Many Requests"
}

const showError= (code) => {
    let text = httpState[code];
    alertdialog.innerHTML =
        '<div role="document" tabindex="0">'+
            '<h2 id="alertTitle">Network Error</h2>'+
            '<p id="alertDesc">'+code+': '+text+'</p>'+
            '<button onclick="emptylist">OK</button>'+
        '</div>';
    alertdialog.showModal();
}

const ucfirst = str => {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

const emptylist = _ => {
    only_pokemon = false;
    remove_top();
    remove_end();
    pokemonslist.innerHTML = '';
}

function insertAfter(e,i){ 
    if(e.nextSibling){ 
        e.parentNode.insertBefore(i,e.nextSibling); 
    } else { 
        e.parentNode.appendChild(i); 
    }
}

const remove_end = _ => {
    const brend = document.querySelector("#brend");
    const end = document.querySelector("#end");
    if (brend != null)
        show.removeChild(brend);
    if (end != null)
        show.removeChild(end);
}

const insert_end = _ => {
    const br = document.createElement('br');
    br.id = "brend"
    const nav = document.createElement('nav'); 
    const a = document.createElement('a');
    nav.id="end";
    a.href="#top";
    a.innerText="Return to the top";
    nav.appendChild(a);
    insertAfter(pokemonslist, br);
    insertAfter(br, nav);
}

const remove_top = _ => {
    const brtop = document.querySelector("#brtop");
    const top = document.querySelector("#top");
    if (brtop != null)
        show.removeChild(brtop);
    if (top != null)
        show.removeChild(top);
}

const insert_top = _ => {
    const br = document.createElement('br');
    br.id = "brtop"
    const nav = document.createElement('nav'); 
    const a = document.createElement('a');
    nav.id="top";
    a.href="#end";
    a.innerText="Go to the end";
    nav.appendChild(a);
    show.insertBefore(br, pokemonslist)
    show.insertBefore(nav, br);
}

const nav_buttons = _ => {
    remove_top();
    remove_end();
    insert_top();
    insert_end();
}

const seedpokemonsform = _ => {
    datalist.innerHTML = '';
    for (let i = 1; i <= MAX_POKEMONS; i++) {
        fetch(url+i)
        .then(response => {
            if (!response.ok)
                throw showError(response.status);
            return response.json();
        })
        .then(response => response["forms"])
        .then(response => response[0])
        .then(data => {
            datalist.innerHTML += '<option value="'+ucfirst(data["name"])+'"/>';
        })
    }
    pokemon.addEventListener('change', getpokemon);
};
  
const getallpokemons = _ => {
    pokemonslist.innerHTML = '';
    one_pokemon = false;
    show.setAttribute("aria-busy", true);
    nav_buttons();
    for(let i = 1; i <= MAX_POKEMONS; i++) {
        fetch(url+i)
        .then(response => {
            if (!response.ok)
                throw showError(response.status);
            return response.json();
        })
        .then(data => {
            let name = ucfirst(data["forms"][0]["name"]);
            pokemonslist.innerHTML += 
            '<div role="listitem">'+
                '<div id="image'+i+'">'+
                    '<image class="responsive-img" loading="lazy"' +'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+i+'"/>'+
                '</div>'+
                '<p>'+name+'</p>'+
                '<div id="info'+i+'" aria-live="polite">'+
                    '<button id="b'+i+'" type="button" onclick="getinfo('+i+')">'+'Info of '+name+'</button>'+
                '</div>'+
                '<br>'+
            '</div>';
        })
    }
    show.setAttribute("aria-busy", false);
};

const getability = _ => {
    pokemonslist.innerHTML = '';

    if (!one_pokemon) {
        remove_end();
        insert_end();
        remove_top();
        insert_top();
        for (let i = 1; i <= MAX_POKEMONS; i++) {
            fetch(url+i)
            .then(response => {
                if (!response.ok)
                    throw showError(response.status);
                return response.json();
            })
            .then(data => {
                pokemonslist.innerHTML += 
                '<div role="listitem">'+
                    '<div id="image">'+
                        '<image class="responsive-img" '+'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+i+'"/>'+
                    '</div>'+
                    '<div id="datability'+i+'">'+
                        '<p>'+"Abilities of "+ucfirst(data["forms"][0]["name"])+'</p>'+
                        '<p>'+"------------------------------"+'</p>'
                    '</div>';
                    let j = 0;
                    while(data["abilities"][j] != null ) {
                        document.querySelector('#datability'+i).innerHTML += '<p>'+(j+1)+". "+data["abilities"][j]["ability"]["name"]+'</p>';
                        j++;
                    }
                +"</div>";
            });
        }
    } else {
        fetch(url+only_pokemon)
        .then(response => {
            if (!response.ok)
                throw showError(response.status);
            return response.json();
        })
        .then(data => {
            pokemonslist.innerHTML += 
            '<div role="listitem">'+
                '<div id="image">'+
                    '<image class="responsive-img" '+'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+data["id"]+'"/>'+
                '</div>'+
                '<div id="datability'+data["id"]+'">'+
                '<p>'+"Abilities of "+ucfirst(data["forms"][0]["name"])+'</p>'+
                '<p>'+"------------------------------"+'</p>'
            '</div>';
            let j = 0;
            while(data["abilities"][j] != null ) {
                document.querySelector('#datability'+i).innerHTML += '<p>'+(j+1)+". "+data["abilities"][j]["ability"]["name"]+'</p>';
                j++;
            }
        +"</div>";
        })
    }
};

const gettype = _ => {
    pokemonslist.innerHTML = '';

    if (!one_pokemon) {
        remove_end();
        insert_end();
        remove_top();
        insert_top();

        for (let i = 1; i <= MAX_POKEMONS; i++) {
            fetch(url+i)
            .then(response => {
                if (!response.ok)
                    throw showError(response.status);
                return response.json();
            })
            .then(data => {
                pokemonslist.innerHTML += 
                '<div role="listitem">'+
                    '<div id="image">'+
                        '<image class="responsive-img" '+'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+i+'"/>'+
                    '</div>'+
                    '<div id="datatype'+i+'">'+
                        '<p>'+"Types of "+ucfirst(data["forms"][0]["name"])+'</p>'+
                        '<p>'+"------------------------------"+'</p>'+
                    '</div>';
                    let j = 0;
                    while(data["types"][j] != null ) {
                        document.querySelector('#datatype'+i).innerHTML += '<p>'+(j+1)+". "+data["types"][j]["type"]["name"]+'</p>';
                        j++;
                    }
                +'</div>';
            })
        }
    } else {
        fetch(url+only_pokemon)
        .then(response => {
            if (!response.ok)
                throw showError(response.status);
            return response.json();
        })
        .then(data => {
            pokemonslist.innerHTML += 
            '<div role="listitem">'+
                '<div id="image">'+
                    '<image class="responsive-img" '+'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+data["id"]+'""/>'+
                '</div>'+
                '<div id="datatype'+data["id"]+'">'+
                    '<p>'+"Types of "+ucfirst(data["forms"][0]["name"])+'</p>'+
                    '<p>'+"------------------------------"+'</p>'
                +'</div>'
                let j = 0;
                while(data["types"][j] != null ) {
                    document.querySelector('#datatype'+i).innerHTML += '<p>'+(j+1)+". "+data["types"][j]["type"]["name"]+'</p>';
                    j++;
                }
            +'</div>';
        }) 
    }
    
};

const getstats = _ => {
    pokemonslist.innerHTML = '';

    if (!one_pokemon) {
        remove_end();
        insert_end();
        remove_top();
        insert_top();
        for (let i = 1; i <= MAX_POKEMONS; i++) {
            fetch(url+i)
            .then(response => {
                if (!response.ok)
                    throw showError(response.status);
                return response.json();
            })
            .then(data => {
                pokemonslist.innerHTML += 
                '<div role="listitem">'+
                    '<div id="image">'+
                        '<image class="responsive-img" '+'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+i+'""/>'+
                    '</div>'+
                    '<div id="datastats'+i+'">'+                    
                        '<p>'+"Stats of "+ucfirst(data["forms"][0]["name"])+'</p>'+
                        '<p>'+"------------------------------"+'</p>'+
                    '</div>';
                    let j = 0;
                    while(data["stats"][j] != null ) {
                        document.querySelector('#datastats'+i).innerHTML += '<p>'+data["stats"][j]["stat"]["name"]
                                            +": "+data["stats"][j]["base_stat"]+'</p>';
                        j++;
                    }
                +'</div>';
            })
        }
    } else {
        fetch(url+only_pokemon)
        .then(response => {
            if (!response.ok)
                throw showError(response.status);
            return response.json();
        })
        .then(data => {
            pokemonslist.innerHTML += 
            '<div role="listitem">'+
                '<div id="image">'+
                    '<image class="responsive-img" '+'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+i+'""/>'+
                '</div>'+
                '<div id="datastats'+data["id"]+'">'+                    
                    '<p>'+"Stats of "+ucfirst(data["forms"][0]["name"])+'</p>'+
                    '<p>'+"------------------------------"+'</p>'+
                '</div>';
                let j = 0;
                while(data["stats"][j] != null ) {
                    document.querySelector('#datastats'+i).innerHTML += '<p>'+data["stats"][j]["stat"]["name"]
                                        +": "+data["stats"][j]["base_stat"]+'</p>';
                    j++;
                }
            +'</div>';
        })
    }
    
};

const getinfo = iter => {
    let info = document.querySelector("#info"+iter);
    info.innerHTML = '';
    info.setAttribute("aria-busy", true);
    fetch(url+iter)
    .then(response => {
        if (!response.ok)
            throw showError(response.status);
        return response.json();
    })
    .then(data => {
        let name = ucfirst(data["forms"][0]["name"]);
        info.innerHTML += '<p>'+"------------------------------"+'</p>';

        // HEIGHT & WEIGHT
        info.innerHTML += '<p> HEIGHT & WEIGHT </p>';
        info.innerHTML += '<p>'+"------------------------------"+'</p>';
        let j = 0;
        if(data["height"] != null )
            info.innerHTML += '<p> Height: '+data["height"]+'</p>';
        else 
            info.innerHTML += '<p> Height: Unknown </p>';

        if(data["weight"] != null )
            info.innerHTML += '<p> Weight: '+data["weight"]+'</p>';
        else 
            info.innerHTML += '<p> Weight: Unknown </p>';
        info.innerHTML += '<p>'+"------------------------------"+'</p>';

        // ABILITIES
        info.innerHTML += '<p> ABILITIES </p>';
        info.innerHTML += '<p>'+"------------------------------"+'</p>';
        j = 0;
        while(data["abilities"][j]!= null ) {
            info.innerHTML += '<p>'+(j+1)+". "+data["abilities"][j]["ability"]["name"]+'</p>';
            j++;
        }
        info.innerHTML += '<p>'+"------------------------------"+'</p>';

        // GAME VERSIONS
        info.innerHTML += '<p> GAME VERSIONS </p>';
        info.innerHTML += '<p>'+"------------------------------"+'</p>';
        j = 0;
        while(data["game_indices"][j]!= null ) {
            info.innerHTML += '<p>'+(j+1)+". Pokemon "+data["game_indices"][j]["version"]["name"]+'</p>';
            j++;
        }
        info.innerHTML += '<p>'+"------------------------------"+'</p>';


        // MOVES
        info.innerHTML += '<p> MOVES </p>';
        info.innerHTML += '<p>'+"------------------------------"+'</p>';
        j = 0;
        while(data["moves"][j]!= null ) {
            info.innerHTML += '<p>'+(j+1)+". "+data["moves"][j]["move"]["name"]+'</p>';
            j++;
        }
        info.innerHTML += '<p>'+"------------------------------"+'</p>';


        // STATS
        info.innerHTML += '<p> STATS </p>';
        info.innerHTML += '<p>'+"------------------------------"+'</p>';
        j = 0;
        while(data["stats"][j] != null ) {
            info.innerHTML += '<p>'+data["stats"][j]["stat"]["name"]
                                +": "+data["stats"][j]["base_stat"]+'</p>';
            j++;
        }
        info.innerHTML += '<p>'+"------------------------------"+'</p>';

        // TYPES
        info.innerHTML += '<p> TYPES </p>';
        info.innerHTML += '<p>'+"------------------------------"+'</p>';
        j = 0;
        while(data["types"][j] != null) {
            info.innerHTML += '<p>'+(j+1)+". "+data["types"][j]["type"]["name"]+'</p>';
            j++;
        }
        info.innerHTML += '<p>'+"------------------------------"+'</p>';

        info.innerHTML += 
        '<div id="close'+iter+'">'+
            '<a href=#image'+iter+'>'+
                '<button id="close" type="button" onclick="_close('+iter+",'"+name+"'"+')">'+"CLOSE"+'</button>'+
            '</a>'+
            '</div>';
        info.setAttribute("aria-busy", false);
    }) 
      
};

const _close = (iter, name) => {
    let info = document.querySelector("#info"+iter);
    info.setAttribute("aria-busy", true);
    info.innerHTML = '<button id="b'+iter+'" type="button" onclick="getinfo('+iter+')">'+'Info of '+name+'</button></div>';
    info.setAttribute("aria-busy", false);
};

const getpokemon = _ => {
    pokemonslist.innerHTML = '';
    remove_top();
    remove_end();
    one_pokemon = true;

    fetch(url+pokemon.value.toLowerCase())
    .then(response => {
        if (!response.ok) {
            one_pokemon = false;
            throw showError(response.status);
        }
        return response.json();
    })
    .then(data => {
        if (data["forms"] == null)
            throw Error("Server returned null");
        
        only_pokemon = data["forms"][0]["name"];
        let name = ucfirst(only_pokemon);
        
        pokemonslist.innerHTML +=
        '<div role="listitem">'+
            '<div id="image'+data["id"]+'">'+
                '<image class="responsive-img" '+'src="'+data["sprites"]["front_shiny"]+'" alt="Logo Pokémon '+data["id"]+'"/>'+
            '</div>'+
            '<p>'+ucfirst(data["forms"][0]["name"])+'</p>'+    
            '<div id="info'+data["id"]+'" aria-live="polite">'+
                '<button id="b'+data["id"]+'" type="button" onclick="getinfo('+data["id"]+')">'+'Info of '+name+'</button>'+
            '</div>';
        '</div>'
    })   
};

const _send = _ => {
    email.value = '';
    subject.value = '';
    message.value = '';
}

h1.addEventListener('click', emptylist);
alertdialog.addEventListener('click', () => alertdialog.close());
document.body.appendChild(alertdialog);
show_all.addEventListener('click', getallpokemons);
ability.addEventListener('click', getability);
type.addEventListener('click', gettype);
stat.addEventListener('click', getstats);
send.addEventListener('click', _send);
seedpokemonsform();