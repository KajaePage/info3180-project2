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
        user_id: localStorage.user_id,
        userdict:{}
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
    },
        computed:
    {
       display: function() 
       {
           return this.userdict['id'];
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