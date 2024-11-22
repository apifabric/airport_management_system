import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {AIRPLANE_MODULE_DECLARATIONS, AirplaneRoutingModule} from  './Airplane-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    AirplaneRoutingModule
  ],
  declarations: AIRPLANE_MODULE_DECLARATIONS,
  exports: AIRPLANE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AirplaneModule { }