<template>
    <div class = "container">
        <div v-if="response.errors != 'novalue'" class = "error-message">
            <ul id="vlist">
                <li v-for="(error, index) in response.errors">
                    {{ error }}
                </li>
            </ul>
        </div>
        <div v-if="response.message != 'novalue'" class = "success-message">
            {{response.message}}
        </div>
        <form method="POST" enctype="multipart/form-data" id = "LoginForm" @submit.prevent="uploadPhoto" class = "formc">
            <ul class="formstf">
                <li class="form-field-1">
                    <label>Username</label>
                    <input v-model="form.username" class="input" type="text"  name = "username">
                </li>

                <li class="form-field-2">
                    <label>Password</label>
                    <input v-model="form.password" class="input" type="text" name = "password">
                </li>

            </ul>
            <button class = "buttonlog" id="submit" type="submit" value="submit" @click.prevent="uploadPhoto()" style="background-color: #0fb881;">Login</button>/>
        </form> 
    </div>
</template>

<script>
export default {
    data() {
      return {
          response: {},
          csrf_token: '',
          form:{
              password: '',
              username: '',
          },
          auth: ''
      }         
    },
    created() {
        this.getCsrfToken();
        //this.logcheck();
    },
     mounted() {
    if (localStorage.token) {
      this.token = localStorage.token;
    }
    if (localStorage.username) {
      this.username = localStorage.username;
    }
    },
    methods:{
        uploadPhoto(){
            let self = this
            let LoginForm = document.getElementById('LoginForm');
            let form_data = new FormData(LoginForm);
            fetch("/api/auth/login", { 
                method : 'POST',
                headers: {
                    'X-CSRF-TOKEN': this.csrf_token
                },
                body: form_data
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
            // display a success message
            self.auth = data.auth;
            console.log(form_data.get('username'))
            localStorage.username = form_data.get('username');
            localStorage.user_id = data['id'];
            localStorage.token = data['token']
            
            console.log(data);
            window.location.href = '/';
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
        logcheck(){
            let self = this;
            fetch('/api/auth/logcheck')
            .then((response)=> response.json())
            .then((data) =>{
                console.log(data);
                self.auth = data.auth;
            })
        },
        containskey(obj, key){
            return Object.keys(obj).includes(key)
        }
         
    },
    computed: {
        haserr() {
            return this.containsKey(this.response, 'errors');
        },
        hasmsg() {
            return this.containsKey(this.response, 'errors');
        }
    }
    

    
}
</script>

<style>
 /* feel free to kill this 
 Temporarily here so that my eyes dont bleed while testing code*/
 .formc{
    margin:10px auto;
    max-width: 400px;
    padding: 20px 12px 10px 20px;
    font: 13px "Lucida Sans Unicode", "Lucida Grande", sans-serif;
  }
  .formc li {
    padding: 0;
    display: block;
    list-style: none;
    margin: 10px 0 0 0;
  }
  .formc label{
    margin:0 0 3px 0;
    padding:0px;
    display:block;
    font-weight: bold;
  }
  
  .formc input,textarea{
      box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    border:1px solid #BEBEBE;
    padding: 7px;
    margin:0px;
    outline: none;
      width: 100%;
  }
  
  .formc textarea{
    height: 100px;
      width: 100%;
  }
  
  .formc .required{
    color:red;
  }
  
  .formc label{
      width:80%;
  }
  
 .formc .button{
      background: #2f4ad0;
      border: none;
      padding: 8px 15px 8px 15px;
    border: none;
      color:white;
  }

  .error-message{
      background-color: #F8D7DA;
      color: #701A22;
  }

  .success-message{
      background-color:#D4EDDA;
      color: #3D7553;
  }
</style>