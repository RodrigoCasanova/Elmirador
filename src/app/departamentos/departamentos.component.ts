import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { FormsModule } from '@angular/forms'; // Para ngModel
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-departamentos',
  imports: [CommonModule, FormsModule,  RouterModule],
  templateUrl: './departamentos.component.html',
  styleUrls: ['./departamentos.component.scss']
})
export class DepartamentosComponent implements OnInit {
  departamentos: any[] = [];
  nuevoDepto: any = {
    CodDepto: '',
    Piso: '',
    Numero: '',
    Estado: 'Disponible',
    RutProp: '',
    Arrendado: false,
    RutArre: '',
    FechaIniC: '',
    FechaFinC: '',
    Observacion: '',
    NumHab: 1
  };

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getDepartamentos().subscribe((data: any) => {
      this.departamentos = data.departamentos;
    });
  }

  crearDepartamento(): void {
    // Aquí enviamos los datos al backend para crear el nuevo departamento
    this.apiService.createDepartamento(this.nuevoDepto).subscribe({
      next: (response) => {
        console.log('Departamento creado con éxito');
        // Recargar la lista de departamentos después de la creación
        this.departamentos.push(this.nuevoDepto);
        // Limpiar los campos del formulario
        this.nuevoDepto = {
          CodDepto: '',
          Piso: '',
          Numero: '',
          Estado: 'Disponible',
          RutProp: '',
          Arrendado: false,
          RutArre: '',
          FechaIniC: '',
          FechaFinC: '',
          Observacion: '',
          NumHab: 1
        };
      },
      error: (err) => {
        console.error('Error al crear departamento:', err);
      }
    });
  }
}
