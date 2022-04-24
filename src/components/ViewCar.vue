<template>
<div class="userdata">
    <a>{{display}}</a>
</div>   
</template>

<script>
export default 
{
    data() {
    return {
        cardict:{}
    };
    },
    created() {
        let self = this
        fetch("/api/cars/<car_id>?id="+localStorage.cid,
         {method: 'GET',headers: {'Authorization': `Bearer: ${localStorage.token}`}})
            .then(function (response) {
                return response.json();
            })
        .then(function (data) {
            // display a success message
            self.cardict = data["car_data"]
            console.log(self.cardict);
        })
        .catch(function (error) {
            console.log(error);
        });
    },
        computed:
    {
       display: function() 
       {
           return this.cardict['id'];
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
}
</script>

<style>
</style>