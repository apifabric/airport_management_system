import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AirportHomeComponent } from './home/Airport-home.component';
import { AirportNewComponent } from './new/Airport-new.component';
import { AirportDetailComponent } from './detail/Airport-detail.component';

const routes: Routes = [
  {path: '', component: AirportHomeComponent},
  { path: 'new', component: AirportNewComponent },
  { path: ':id', component: AirportDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Airport-detail-permissions'
      }
    }
  },{
    path: ':airport_id/Airplane', loadChildren: () => import('../Airplane/Airplane.module').then(m => m.AirplaneModule),
    data: {
        oPermission: {
            permissionId: 'Airplane-detail-permissions'
        }
    }
},{
    path: ':arrival_airport_id/Flight', loadChildren: () => import('../Flight/Flight.module').then(m => m.FlightModule),
    data: {
        oPermission: {
            permissionId: 'Flight-detail-permissions'
        }
    }
},{
    path: ':departure_airport_id/Flight', loadChildren: () => import('../Flight/Flight.module').then(m => m.FlightModule),
    data: {
        oPermission: {
            permissionId: 'Flight-detail-permissions'
        }
    }
}
];

export const AIRPORT_MODULE_DECLARATIONS = [
    AirportHomeComponent,
    AirportNewComponent,
    AirportDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AirportRoutingModule { }