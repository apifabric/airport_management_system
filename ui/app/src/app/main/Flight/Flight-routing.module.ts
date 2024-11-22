import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FlightHomeComponent } from './home/Flight-home.component';
import { FlightNewComponent } from './new/Flight-new.component';
import { FlightDetailComponent } from './detail/Flight-detail.component';

const routes: Routes = [
  {path: '', component: FlightHomeComponent},
  { path: 'new', component: FlightNewComponent },
  { path: ':id', component: FlightDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Flight-detail-permissions'
      }
    }
  },{
    path: ':flight_id/Passenger', loadChildren: () => import('../Passenger/Passenger.module').then(m => m.PassengerModule),
    data: {
        oPermission: {
            permissionId: 'Passenger-detail-permissions'
        }
    }
}
];

export const FLIGHT_MODULE_DECLARATIONS = [
    FlightHomeComponent,
    FlightNewComponent,
    FlightDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FlightRoutingModule { }