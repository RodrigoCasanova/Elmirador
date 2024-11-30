import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GastosComunesComponent } from './gastos-comunes.component';

describe('GastosComunesComponent', () => {
  let component: GastosComunesComponent;
  let fixture: ComponentFixture<GastosComunesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GastosComunesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GastosComunesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
