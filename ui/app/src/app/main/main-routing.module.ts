import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Airplane', loadChildren: () => import('./Airplane/Airplane.module').then(m => m.AirplaneModule) },
    
        { path: 'Airport', loadChildren: () => import('./Airport/Airport.module').then(m => m.AirportModule) },
    
        { path: 'Flight', loadChildren: () => import('./Flight/Flight.module').then(m => m.FlightModule) },
    
        { path: 'Passenger', loadChildren: () => import('./Passenger/Passenger.module').then(m => m.PassengerModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }