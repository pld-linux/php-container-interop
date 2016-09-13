<?php
/**
 * Autoloader for php-container-interop and its' dependencies
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!isset($loader) || !($loader instanceof \Symfony\Component\ClassLoader\ClassLoader)) {
    if (!class_exists('Symfony\\Component\\ClassLoader\\ClassLoader', false)) {
        require_once '/usr/share/php/Symfony/Component/ClassLoader/ClassLoader.php';
    }

    $loader = new \Symfony\Component\ClassLoader\ClassLoader();
    $loader->register();
}

$loader->addPrefix('Interop\\Container\\', dirname(dirname(__DIR__)));

return $loader;
