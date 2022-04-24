<template>
<div class="userdata">
    <img :src="getImgUrl(display.photo)" class="card-img">
    <h3>{{ display.name }}</h3>
    <h3>@{{ display.username}}</h3>
    <p>{{ display.biography }}</p>
    <p>Email: {{ display.email }}</p>
    <p>Location: {{ display.location }}</p>
    <p>Joined: {{ display.date_joined }}</p>
    <p>{{cardisplay}}</p>
</div>  
         
</template>

<script>
export default 
{
    data() {
    return {
        user_id: localStorage.user_id,
        userdict:{},
        carlist:null,
        url:''
    };
    },
    created() {
        let self = this
        fetch("/api/users/<user_id>?id="+localStorage.user_id,
         {method: 'GET',headers: {'Authorization': `Bearer: ${localStorage.token}`}})
            .then(function (response) {
                return response.json();
            })
        .then(function (data) {
            // display a success message
            self.userdict = data["user_data"]
            console.log(self.userdict);
        })
        .catch(function (error) {
            console.log(error);
        });
        fetch("/api/users/<user_id>/favourites?id="+localStorage.user_id,
         {method: 'GET',headers: {'Authorization': `Bearer: ${localStorage.token}`}})
            .then(function (response) {
                console.log('here')
                return response.json();
            })
        .then(function (data) {
            // display a success message
            self.carlist = data["favdata"]
            console.log(self.carlist);
        })
        .catch(function (error) {
            console.log(error);
        });
    },
        computed:
    {
       display: function() 
       {
           return this.userdict;
       },
       cardisplay: function()
       {
           return this.carlist;
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
    methods:{
        getImgUrl(pet) {
            self.url = './uploads/' + pet
            if (! url) {
                return ''; //or perhaps a placeholder loading image 
            }
            return self.url
        }    
    }
}
</script>

<style>
</style>