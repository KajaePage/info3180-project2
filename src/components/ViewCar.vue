<template>
<!-- <div class="userdata">
    <a>{{display}}</a>
</div>    -->
<div class="card mb-3" >
    <div class="row no-gutters">
      <div class="col-md-4">
        <img :src="getImgUrl(display.photo)" class="card-img">
      </div>
      <div class="col-md-8">
        <div class="card-body">
            <h5 class="card-title">{{display.year}} {{display.make}}</h5>
            <div class = "tags">
                <span class="tag">${{display.price}}</span>
                <span class="tag">{{display.car_type}}</span>
            </div>
            
            <p class="card-text">{{display.desc}}</p>
            <div class="rbth">
                <span class="tag">{{display.colour}} </span>
                <span class="tag">{{display.transmission}} </span>
            </div>
            <span class="tag">{{display.model}}</span>
            <div class = "bhold">
                <button class="pbut">Email Owner</button>
                <button class="pbut" @click="add_to_fav()">Add to Fav</button>
            </div>
            
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default 
{
    data() {
    return {
        car:{},
        url: ''
    };
    },
    created() {
        let self = this
        this.getCsrfToken();
        this.fgetsCars()
    },
        computed:
    {
       display: function() 
       {
           return this.car;
       }
    },
    mounted() {
     window.onbeforeunload = () => {
    }    
    if (localStorage.token) {
      this.token = localStorage.token;
      console.log(this.token)
    }
    if (localStorage.username) {
      this.username = localStorage.username;
    }
    },
    methods: {
        getImgUrl(pet) {
            self.url = '../uploads/' + pet
            if (! url) {
                return ''; //or perhaps a placeholder loading image 
            }
            return self.url
        },
        async fgetsCars(){
            let self = this
            fetch("/api/cars/<car_id>?id="+localStorage.cid,
        {method: 'GET',headers: {'Authorization': `Bearer: ${localStorage.token}`}})
            .then(function (response) {
                return response.json();
            })
        .then(function (data) {
            // display a success message
            self.car = data["car_data"]
            console.log(self.car);
        })
        .catch(function (error) {
            console.log(error);
        });
        },
        getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
            .then((response)=> response.json())
            .then((data) =>{
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
        },
        add_to_fav(){
            fetch('/api/cars/<car_id>/favourite?car_id=' + localStorage.cid, {
                method: 'POST',
                headers: {
                'Authorization': `Bearer: ${this.token}`,
                'X-CSRF-TOKEN': this.csrf_token
                }
            })
            .then(function(response) {
            return response.json();
            })
            .then(function(data) {
                console.log(data)
                self.carlist = data.carlist;
            });
        }
    }
}
</script>

<style>
    .plist{
    display: grid;
 
    grid-template-columns: repeat(3, 1fr);
    
    grid-auto-rows: auto;
    
    grid-gap: 1rem;
    
    list-style-type: none;
}
.card {

    background-color: white;
    border: 1px solid #bacdd8;
    padding: 8px;
    border-radius: 12px;
  }

.plist li img{
    width: 100%;
    height: 214px;
    object-fit: cover;
}

.pname {
    font-size: 24px;
    font-weight: 600;
  
    margin-top: 16px;
  }

.tag {
    padding: 4px 8px;
    border: 1px solid #e5eaed;
  
    border-radius: 50px;
    font-size: 12px;
    font-weight: 600;
    color: #788697;
    margin-bottom: 160px;
  }

  .plocat {
    font-size: 14px;
    color: #7f8c9b;
    
  }

  .pbut {
    border: none;
    padding: 12px 24px;
    border-radius: 50px;
  
    font-weight: 600;
    color: #0077ff;
    background-color: #e0efff;
  

    margin: 15px auto;
    display: block;
    text-align: center;
  
    cursor: pointer;
    text-decoration: none;
  }

  .card-text {
    margin-top:10px;
  }

  .card.mb-3{
    max-width: 100%; 
    height: 2fr;
  }

  .card-img{
    width: 100%;
  }

  .col-md-4{
    max-width: 60%;
  }

  .rbth {
    margin-bottom: 10px;
  }
  .card-body .pbut{
    display: inline;
  }

  .card__details {
    padding: 16px 8px 8px 8px;
  }

</style>