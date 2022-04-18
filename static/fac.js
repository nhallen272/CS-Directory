console.log('hello world')

const HTMLrow = document.getElementById('faculty-row')
const modalBody = document.getElementById('modal-body')

`<img src="{{ fac.pic }}" /> 
            <h5>Title: {{ fac.title }}</h5>
            <h6>Research Types:</h6>
            {% for cat in fac.research.all %}
                <a href="#" class="badge badge-pill badge-secondary">{{ cat.title }}</a>
            {% endfor %}
            <h5>About Me</h5>  
            <p>{{ fac.bio }}</p>
            <h6>Contact</h6> 
            <h5>Email: {{ fac.email }}</h5>
            <h5>Phone: {{ fac.phone }}</h5>
            <h5>Website: {{ fac.website }}</h5>
`

//<p class="card-text">{{ fac.bio|truncatechars:80 }}...</p>

$.ajax ({
  type: 'GET',
  url: '/facview/',
  success: function(response){
    console.log(response)
    const data = JSON.parse(response.data)
    console.log(data)
    data.forEach(el=>{
      console.log(el.fields)
      HTMLrow.innerHTML += `
        <div class="col-md-4">
        <div class="card mb-2">
            <div data-bs-toggle="modal" data-bs-target="#fac-modal"><img class="card-img-top" src="${el.pic}"></div>
            <div class="card-body">
                <h5 class="card-title">{{ fac.name }}</h5>
                <h6 class="card-subtitle mb-2 text-muted">${el.heading}</h6>
                
                <h6>Email: ${el.email}</h6>
                <h6>Phone: ${el.phone }</h6>
                <!-- Button trigger modal -->
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#fac-modal">
                    More Info
                </button>
              `
    })
  },
  error: function(error){
    console.log(error)
  }
})