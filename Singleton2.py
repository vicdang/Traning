public class Singleton {
    private static Singleton uniqueInstance;
    // other useful instance variables here
    private Singleton() {}
    public static Singleton getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }
    // other useful methods here
}


    Tạo một private static instance của singleton class đó, đây chính là instance duy nhất của class này
    Tạo private constructor, không cho phép tạo mới instance từ bên ngoài singleton class
    Tạo một public static method giúp những class bên ngoài lấy ra instance duy nhất của singleton class này
