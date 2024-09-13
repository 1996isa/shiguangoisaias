using System;
using System.Collections.Generic;


class CatalogoRevistas
    {
        static
    void
    Main()
    {
    //Crear
    catálogo
    de
    revistas
    List < string > catalogo = new
    List < string > ();

    //Ingresar
    10
    títulos
    de
    revistas
    Console.WriteLine("Ingrese 10 títulos de revistas:");
    for (int i = 0; i < 10; i++)
    {
        Console.Write($"Título {i + 1}: ");
    string titulo = Console.ReadLine();
    catalogo.Add(titulo);
    }

    //Menú para buscar un título
    bool salir = false;


while (!salir)
    {
        Console.WriteLine("\n--- Menú ---");
    Console.WriteLine("1. Buscar título (Iterativa)");
    Console.WriteLine("2. Buscar título (Recursiva)");
    Console.WriteLine("3. Salir");
    Console.Write("Seleccione una opción: ");
    string
    opcion = Console.ReadLine();

    switch(opcion)
    {
        case
    "1": \
        Console.Write("Ingrese el título a buscar (Iterativa): ");
    string
    tituloBuscarIterativa = Console.ReadLine();
    bool
    encontradoIterativa = BuscarTituloIterativa(catalogo, tituloBuscarIterativa);
    Console.WriteLine(encontradoIterativa ? "Encontrado": "No encontrado");
    break;

    case
    "2":
    Console.Write("Ingrese el título a buscar (Recursiva): ");
    string
    tituloBuscarRecursiva = Console.ReadLine();
    bool
    encontradoRecursiva = BuscarTituloRecursiva(catalogo, tituloBuscarRecursiva, 0);
    Console.WriteLine(encontradoRecursiva ? "Encontrado": "No encontrado");
    break;

case
"3":
salir = true;
break;

default:
Console.WriteLine("Opción no válida. Intente de nuevo.");
break;
}
}
}

//Búsqueda
iterativa
static
bool
BuscarTituloIterativa(List < string > catalogo, string
titulo)
{
    foreach(string
item in catalogo)
{
if (item.Equals(titulo, StringComparison.OrdinalIgnoreCase))
{
return true;
}
}
return false;
}

//Búsqueda
recursiva
static
bool
BuscarTituloRecursiva(List < string > catalogo, string
titulo, int
index)
{
if (index >= catalogo.Count)
    {
return false;
}
if (catalogo[index].Equals(titulo, StringComparison.OrdinalIgnoreCase))
{
return true;
}
return BuscarTituloRecursiva(catalogo, titulo, index + 1);
}
}
