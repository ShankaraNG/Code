import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { registerComponent } from './register/register.component';
import { HomePageComponent } from './home-page/home-page.component';
import { ForgotpasswordComponent } from './forgotpassword/forgotpassword.component';
import { RecommendedComponent } from './recommended/recommended.component';
import { FavouriteComponent } from './favourite/favourite.component';
import { LogoutComponent } from './logout/logout.component';
import { DeleteComponent } from './delete/delete.component';
import { AccountComponent } from './account/account.component';

const routes: Routes = [
 // {path:'',component:registerComponent},
  {path: '',component:HomePageComponent},
  {path: "home-page",component:HomePageComponent},
  {path:"register",component:registerComponent},
  {path:"login",component:LoginComponent},
  {path:"forgotpassword",component:ForgotpasswordComponent},
  {path:"recommended", component:RecommendedComponent},
  {path:"favourite", component:FavouriteComponent},
  {path: "logout", component:LogoutComponent},
  {path: "delete", component:DeleteComponent},
  {path: "account", component:AccountComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
