import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Airplane-new',
  templateUrl: './Airplane-new.component.html',
  styleUrls: ['./Airplane-new.component.scss']
})
export class AirplaneNewComponent {
  @ViewChild("AirplaneForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}