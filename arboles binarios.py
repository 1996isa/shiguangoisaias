import public

using


}
class Nodo
{
    public int Valor;
    public Nodo Izquierdo, Derecho;

    public Nodo(int valor)
    {
        Valor = valor;
        Izquierdo = Derecho = null;
    }
}

class ArbolBinario
{
    public Nodo Raiz;

    public ArbolBinario()
    {
        Raiz = null;
    }

    // Insertar nodo en el árbol
    public void Insertar(int valor)
    {
        Raiz = InsertarRecursivo(Raiz, valor);
    }

    private Nodo InsertarRecursivo(Nodo nodo, int valor)
    {
        if (nodo == null)
        {
            nodo = new Nodo(valor);
            return nodo;
        }

        if (valor < nodo.Valor)
            nodo.Izquierdo = InsertarRecursivo(nodo.Izquierdo, valor);
        else if (valor > nodo.Valor)
            nodo.Derecho = InsertarRecursivo(nodo.Derecho, valor);

        return nodo;
    }

    // Búsqueda de un valor en el árbol
    public bool Buscar(int valor)
    {
        return BuscarRecursivo(Raiz, valor);
    }

    private bool BuscarRecursivo(Nodo nodo, int valor)
    {
        if (nodo == null)
            return false;

        if (nodo.Valor == valor)
            return true;
        else if (valor < nodo.Valor)
            return BuscarRecursivo(nodo.Izquierdo, valor);
        else
            return BuscarRecursivo(nodo.Derecho, valor);
    }

    // Recorridos: Inorden, Preorden, Postorden
    public void Inorden()
    {
        InordenRecursivo(Raiz);
        Console.WriteLine();
    }

    private void InordenRecursivo(Nodo nodo)
    {
        if (nodo != null)
        {
            InordenRecursivo(nodo.Izquierdo);
            Console.Write(nodo.Valor + " ");
            InordenRecursivo(nodo.Derecho);
        }
    }

    public void Preorden()
    {
        PreordenRecursivo(Raiz);
        Console.WriteLine();
    }

    private void PreordenRecursivo(Nodo nodo)
    {
        if (nodo != null)
        {
            Console.Write(nodo.Valor + " ");
            PreordenRecursivo(nodo.Izquierdo);
            PreordenRecursivo(nodo.Derecho);
        }
    }

    public void Postorden()
    {
        PostordenRecursivo(Raiz);
        Console.WriteLine();
    }

    private void PostordenRecursivo(Nodo nodo)
    {
        if (nodo != null)
        {
            PostordenRecursivo(nodo.Izquierdo);
            PostordenRecursivo(nodo.Derecho);
            Console.Write(nodo.Valor + " ");
        }
    }

    // Eliminar un nodo del árbol
    public void Eliminar(int valor)
    {
        Raiz = EliminarRecursivo(Raiz, valor);
    }

    private Nodo EliminarRecursivo(Nodo nodo, int valor)
    {
        if (nodo == null)
            return nodo;

        if (valor < nodo.Valor)
            nodo.Izquierdo = EliminarRecursivo(nodo.Izquierdo, valor);
        else if (valor > nodo.Valor)
            nodo.Derecho = EliminarRecursivo(nodo.Derecho, valor);
        else
        {
            if (nodo.Izquierdo == null)
                return nodo.Derecho;
            else if (nodo.Derecho == null)
                return nodo.Izquierdo;

            nodo.Valor = ValorMinimo(nodo.Derecho);
            nodo.Derecho = EliminarRecursivo(nodo.Derecho, nodo.Valor);
        }

        return nodo;
    }

    private int ValorMinimo(Nodo nodo)
    {
        int minv = nodo.Valor;
        while (nodo.Izquierdo != null)
        {
            minv = nodo.Izquierdo.Valor;
            nodo = nodo.Izquierdo;
        }
        return minv;
    }
}

class Program
{
    static void Main()
    {
        ArbolBinario arbol = new ArbolBinario();
        int opcion, valor;

        do
        {
            Console.WriteLine("----- Menú de Árbol Binario -----");
            Console.WriteLine("1. Insertar nodo");
            Console.WriteLine("2. Buscar nodo");
            Console.WriteLine("3. Mostrar en inorden");
            Console.WriteLine("4. Mostrar en preorden");
            Console.WriteLine("5. Mostrar en postorden");
            Console.WriteLine("6. Eliminar nodo");
            Console.WriteLine("0. Salir");
            Console.Write("Seleccione una opción: ");
            opcion = int.Parse(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    Console.Write("Ingrese el valor a insertar: ");
                    valor = int.Parse(Console.ReadLine());
                    arbol.Insertar(valor);
                    break;
                case 2:
                    Console.Write("Ingrese el valor a buscar: ");
                    valor = int.Parse(Console.ReadLine());
                    bool encontrado = arbol.Buscar(valor);
                    Console.WriteLine(encontrado ? "Valor encontrado" : "Valor no encontrado");
                    break;
                case 3:
                    Console.WriteLine("Recorrido en Inorden:");
                    arbol.Inorden();
                    break;
                case 4:
                    Console.WriteLine("Recorrido en Preorden:");
                    arbol.Preorden();
                    break;
                case 5:
                    Console.WriteLine("Recorrido en Postorden:");
                    arbol.Postorden();
                    break;
                case 6:
                    Console.Write("Ingrese el valor a eliminar: ");
                    valor = int.Parse(Console.ReadLine());
                    arbol.Eliminar(valor);
                    break;
                case 0:
                    Console.WriteLine("Saliendo...");
                    break;
                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }

        } while (opcion != 0);
    }
}
