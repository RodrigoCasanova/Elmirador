import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarGastosPendientesComponent } from './listar-gastos-pendientes.component';

describe('ListarGastosPendientesComponent', () => {
  let component: ListarGastosPendientesComponent;
  let fixture: ComponentFixture<ListarGastosPendientesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListarGastosPendientesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListarGastosPendientesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
