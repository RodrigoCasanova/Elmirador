import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { DepartamentosComponent } from './departamentos/departamentos.component';
import { GastosComunesComponent } from './gastos-comunes/gastos-comunes.component';
import { MarcarComoPagadoComponent } from './marcar-como-pagado/marcar-como-pagado.component';
import { ListarGastosPendientesComponent } from './listar-gastos-pendientes/listar-gastos-pendientes.component';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' }, // Redirige la raíz a 'home'
  { path: 'home', component: HomeComponent }, // Ruta para HomeComponent
  { path: 'departamentos', component: DepartamentosComponent }, // Ruta para Departamentos
  { path: 'gastos-comunes', component: GastosComunesComponent }, // Ruta para Gastos Comunes
  { path: 'marcar-como-pagado', component: MarcarComoPagadoComponent },
  { path: 'listar-gastos-pendientes', component: ListarGastosPendientesComponent },
];
